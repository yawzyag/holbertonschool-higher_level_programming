#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
	{
		return (0);
	}
	else
	{
		slow = list->next;
		fast = list->next->next;
		while (slow && fast)
		{
			if (slow == fast)
			{
				return (1);
			}
			slow = slow->next;
			fast = fast->next->next;
		}
	}
	return (0);
}
