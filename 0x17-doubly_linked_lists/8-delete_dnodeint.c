#include "lists.h"
/**
 * delete_dnodeint_at_index - delets a node at a specific index
 *
 * @head: the head of the linked list
 * @index: the index at which to delete a node
 * Return: 1 on success -1 else
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *ptr = *head, *hold;
	unsigned int i = 0;

	if (index == 0 && *head != NULL)
	{
		hold = (**head).next;
		free(*head);
		*head = hold;
		return (1);
	}
	while (*head != NULL)
	{
		if (i == index && (**head).next != NULL)
		{
			((**head).prev)->next = (**head).next;
			((**head).next)->prev = (**head).prev;
			free(*head);
			*head = ptr;
			return (1);
		}
		else if (i == index && (**head).next == NULL)
		{
			((**head).prev)->next = NULL;
			free(*head);
			*head = ptr;
			return (1);
		}
		*head = (**head).next;
		i++;
	}
	return (-1);
}
