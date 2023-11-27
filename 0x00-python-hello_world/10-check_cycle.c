#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list contains a cycle.
 *
 *@list: singly linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
listint_t *fast;
listint_t *slow;

if (list == NULL || list->next == NULL)
return (0);

slow = list;
fast = list;

while (slow && fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;
if (slow == fast)
return (1);
}
return (0);
}
