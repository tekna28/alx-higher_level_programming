#include"lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 *@head: pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
listint_t *current = *head;
static listint_t *temp;

if (current == NULL)
return (1);

if (temp == NULL)
temp = current;

if (is_palindrome(&current->next) && temp->n == current->n)
{
temp = temp->next;
return (1);
}
else
return (0);
}
