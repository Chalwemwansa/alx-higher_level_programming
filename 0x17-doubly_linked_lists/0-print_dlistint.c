#include "lists.h"
/**
 * print_dlistint - printd the contents of a linked list from head to the tail
 *
 * @h: the linked list head passed as parameter
 * Return: return the number of nodes in the linked list
 */
size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *ptr = h;
	size_t i = 0;

	while (ptr != NULL)
	{
		printf("%d\n", (*ptr).n);
		ptr = (*ptr).next;
		i++;
	}
	return (i);
}
