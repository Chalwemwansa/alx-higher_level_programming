#include "lists.h"
/**
 * get_dnodeint_at_index - gets  node at a given index from a linked list
 *
 * @head: the head of the linked list
 * @index: the index from which to get the element
 * Return: the address of the node at the index
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	unsigned int i = 0;
	dlistint_t *ptr = head;

	while (ptr != NULL)
	{
		if (i == index)
			return (ptr);
		ptr = (*ptr).next;
		i++;
	}
	return (NULL);
}
