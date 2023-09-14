#include "lists.h"
/**
 * add_dnodeint - adds a node to the begining of the linked list
 *
 * @head: the starting memory address to start with
 * @n: the value to be put at the beginning off the linked list
 * Return: address of the new node
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new_node;

	new_node = malloc(sizeof(dlistint_t));
	if (new_node == NULL)
	{
		printf("malloc failed");
		return (NULL);
	}
	(*new_node).n = n;
	if (*head != NULL)
	{
		(**head).prev = new_node;
		(*new_node).next = *head;
	}
	else
		(*new_node).next = NULL;
	(*new_node).prev = NULL;
	*head = new_node;
	return (new_node);
}
