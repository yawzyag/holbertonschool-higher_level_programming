#include "lists.h"

/**
 * insert_node - insert node linked list sorted
 * @head: linked list
 * @number: number to insert
 * Return: linked list head
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current_node;
	unsigned int idx;

	if (!head)
		return (0);
	idx = 0;
	current_node = *head;
	while (current_node->n < number)
	{
		idx++;
		current_node = current_node->next;
	}
	new_node = (listint_t *)malloc(sizeof(listint_t));
	if (!new_node)
		return (0);
	new_node->n = number;
	if (*head == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}
	if (idx == 0)
	{ new_node->next = *head;
		*head = new_node;
		return (new_node); }
	current_node = *head;
	while (idx - 1 > 0)
	{
		if (!current_node)
		{ free(new_node);
			return (0); }
		current_node = current_node->next;
		idx--;
	}
	new_node->next = current_node->next;
	current_node->next = new_node;
	return (new_node);
}
