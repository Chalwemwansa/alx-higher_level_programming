#include "lists.h"
/**
 * is_palindrome -  checks if a linked list is a palindrome or not
 *
 * @head: the begining of the linked list
 * Return: 0 if palindrome, else 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr1;
	int *ptr, length, i = 0;
	
	if (head == NULL || *head == NULL)
		return (1);
	ptr1 = *head;
	while (ptr1 != NULL)
	{
		i++;
		ptr1 = (*ptr1).next;
	}
	ptr = malloc(sizeof(int) * (i + 1));
	if (ptr == NULL)
		return (0);
	ptr1 = *head;
	length = i - 1;
	for (i = 0; i <= length; i++)
	{
		ptr[i] += (*ptr1).n;
		ptr1 = (*ptr1).next;
	}
	for (i = 0; i <= length / 2; i++)
	{
		if (ptr[i] != ptr[(length - i)])
		{
			free(ptr);
			return (0);
		}
	}
	free(ptr);
	return (1);
}
