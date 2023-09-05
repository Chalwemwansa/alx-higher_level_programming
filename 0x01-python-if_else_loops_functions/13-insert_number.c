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
	listint_t *ptr, *new;

	if (head == NULL || *head == NULL)
		return (NULL);
	ptr = (**head).next;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	(**head).next = new;
	(*new).n = number;
	(*new).next = ptr;
	return (new);
}
