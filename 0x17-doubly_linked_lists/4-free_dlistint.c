#include "lists.h"
/**
 * free_dlistint - frees a dlistint_t linked list
 *
 * @head: the head of the linked list to be freed
 * Return: void, does not return anything
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *hold;

	while (head != NULL)
	{
		hold = (*head).next;
		free(head);
		head = hold;
	}
}
