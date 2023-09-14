#include "lists.h"
/**
 * dlistint_len - printd the contents of a linked list from head to the tail
 *
 * @h: the linked list head passed as parameter
 * Return: return the number of nodes in the linked list
 */
size_t dlistint_len(const dlistint_t *h)
{
	const dlistint_t *ptr = h;
	size_t i = 0;

	while (ptr != NULL)
	{
		ptr = (*ptr).next;
		i++;
	}
	return (i);
}
