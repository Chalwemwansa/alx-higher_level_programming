#include "lists.h"
/**
 * insert_dnodeint_at_index - inserts a node at a given index in a linked list
 *
 * @h: the head of the doubly linked list
 * @idx: the index to insert the new node
 * @n: the value for the new node
 * Return: the address of the new node inserted
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *ptr = *h, *new_node, *hold;
	unsigned int i = 0;

	new_node = malloc(sizeof(dlistint_t));
	if (new_node == NULL)
		return (NULL);

	(*new_node).n = n;
	if (*h == NULL)
	{
		(*new_node).prev = NULL;
		(*new_node).next = NULL;
		*h = new_node;
		return (new_node);
	}
	else if (idx == 0)
	{
		(*new_node).prev = NULL;
		(*new_node).next = *h;
		(**h).prev = new_node;
		*h = new_node;
		return (new_node);
	}

	while (*h != NULL)
	{
		if (((**h).next != NULL) && (i == (idx - 1)))
		{
			hold = (**h).next;
			(**h).next = new_node;
			(*new_node).prev = *h;
			*h = hold;
			(*new_node).next = *h;
			(**h).prev = new_node;
			*h = ptr;
			return (new_node);
		}
		if ((**h).next == NULL && i == (idx - 1))
			break;
		else if ((**h).next == NULL && i != (idx - 1))
		{
			*h = ptr;
			free(new_node);
			return (NULL);
		}
		*h = (**h).next;
		i++;
	}
	(**h).next = new_node;
	(*new_node).prev = *h;
	(*new_node).next = NULL;
	*h = ptr;
	return (new_node);

}
