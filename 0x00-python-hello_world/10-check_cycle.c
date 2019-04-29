#include "lists.h"

/**
 * check_cycle - chech for cycle in loinked list
 * @list: pointer to head of list
 * Return: 1 if coincidence 0 else
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
			slow = slow->next;
			fast = fast->next->next;
			if (slow == fast)
			{
				return (1);
			}
		}
	}
	return (0);
}
