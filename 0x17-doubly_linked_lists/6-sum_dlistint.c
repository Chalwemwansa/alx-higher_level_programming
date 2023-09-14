#include "lists.h"
/**
 * sum_dlistint - returns the sum of all the integers in the linke list
 *
 * @head: the head of the linked list
 * Return: an integer
 */
int sum_dlistint(dlistint_t *head)
{
	dlistint_t *ptr = head;
	int sum = 0;

	while (ptr != NULL)
	{
		sum += (*ptr).n;
		ptr = (*ptr).next;
	}
	return (sum);
}
