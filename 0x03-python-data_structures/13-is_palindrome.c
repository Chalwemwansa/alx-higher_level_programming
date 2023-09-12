#include "lists.h"
/**
 * is_palindrome -  checks if a linked list is a palindrome or not
 *
 * @head: the begining of the linked list
 * Return: 0 if palindrome, else 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr1 = *head;
	int *ptr, length, i = 0;
	
	if (head == NULL || *head == NULL)
		return (1);
	while (ptr1 != NULL)
	{
		i++;
		ptr1 = (*ptr1).next;
	}
	ptr = malloc(sizeof(int) * i);
	length = i - 1;
	while (ptr1 != NULL)
	{
		ptr += (*ptr1).n;
		ptr1 = (*ptr1).next;
	}
	for (i = 0; i <= (length / 2); i++)
		if (ptr[i] != ptr[(length - i)])
				return (0);
	return (1);
}
