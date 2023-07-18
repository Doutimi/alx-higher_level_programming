#include "lists.h"
#include <stddef.h>

int is_palindrome(listint_t **head)
{
if (head == NULL || *head == NULL)
	return (1);

listint_t *current = *head;
int length = 0;
while (current != NULL)
	{
	current = current->next;
	length++;
	}

current = *head;
int content[length];
int a = 0;
while (current != NULL)
	{
	content[a] = current->n;
	current = current->next;
	a++;
	}

int start = 0;
int end = length - 1;
while (start < end)
	{
	if (content[start] != content[end])
		return (0);

	start++;
	end--;
	}

	return (1);
}
