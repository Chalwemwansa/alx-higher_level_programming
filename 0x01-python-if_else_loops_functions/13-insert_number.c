#include "lists.h"
/**
 * insert_node - inserts a node into a linked list
 *
 * @head: the head of the linked list
 * @number: number to be inserted into the linked list
 * Return: a listint_t pointer
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *new, *headptr;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if (*head == NULL)
	{
		(*new).n = number;
		(*new).next = NULL;
		*head = new;
		return (new);
	}
	if ((**head).n > number)
	{
		(*new).n = number;
		(*new).next = *head;
		*head = new;
		return (new);
	}
	headptr = *head;
	while ((*headptr).next != NULL)
	{
		ptr = (*headptr).next;
		if ((*ptr).n >= number)
		{
			(*headptr).next = new;
			(*new).n = number;
			(*new).next = ptr;
			return (new);
		}
		headptr = (*headptr).next;
	}
	(*headptr).next = new;
	(*new).n = number;
	(*new).next = NULL;
	return (new);
}
