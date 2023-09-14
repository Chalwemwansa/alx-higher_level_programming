#include "lists.h"
#define LIST_NULL 0
#define LIST_NOT_NULL 1
/**
 * add_dnodeint_end - adds a node at the end of the linked list
 *
 * @head: the head of the linked list
 * @n: the value to be added to the end of the linked list
 * Return: the adress of the new element
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new_node, *ptr = *head;
	int flag = LIST_NULL;

	new_node = malloc(sizeof(dlistint_t));
	if (new_node == NULL)
	{
		printf("Malloc failed");
		return (NULL);
	}
	(*new_node).n = n;
	(*new_node).next = NULL;
	while (*head != NULL)
	{
		flag = LIST_NOT_NULL;
		if ((**head).next == NULL)
		{
			(**head).next = new_node;
			(*new_node).prev = *head;
			*head = ptr;
			break;
		}
		*head = (**head).next;
	}
	if (flag == LIST_NULL)
	{
		(*new_node).prev = NULL;
		*head = new_node;
	}
	return (new_node);
}
