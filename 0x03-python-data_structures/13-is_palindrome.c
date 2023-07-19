#include "lists.h"
#include <stddef.h>

int is_palindrome(listint_t **head)
{
listint_t *current;
int length = 0;
int content;
int start = 0;
int a, end;

if (head == NULL || *head == NULL)
	return (1);

current = *head;
while (current != NULL)
	{
	current = current->next;
	length++;
	}

current = *head;
a = 0;
while (current != NULL)
	{
	content[a] = current->n;
	current = current->next;
	a++;
	}

end = length - 1;
while (start < end)
	{
	if (content[start] != content[end])
		return (0);

	start++;
	end--;
	}

	return (1);
}
