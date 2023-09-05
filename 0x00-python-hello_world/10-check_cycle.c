#include "lists.h"
/**
 * check_cycle - function that checks if structure has a cycle
 * @list: the structure passed as argument
 * Return: 0 if no cycle, else 1
 */
int check_cycle(listint_t *list)
{
	int j, i;
	listint_t *head, *check, *tail;

	if (list == NULL)
		return (0);
	head = list;
	check = list;
	tail = (*list).next;
	for (i = 0; (*tail).next != NULL && tail != NULL; i++)
	{
		for (j = 0; j <= i; j++)
		{
			if ((*tail).next == check)
				return (1);
			check = (*check).next;
		}
		tail = (*tail).next;
		check = head;
	}
	return (0);
}
