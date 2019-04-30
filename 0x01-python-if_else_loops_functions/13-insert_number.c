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
	listint_t *aux;

	if (!head)
		return (0);
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
	if (number == 0)
	{ new_node->next = *head;
		*head = new_node;
		return (new_node); }
	current_node = *head;
	while (current_node->n < number)
	{
		if (!current_node)
		{ free(new_node);
			return (0); }
		aux = current_node;
		current_node = current_node->next;
	}
	new_node->next = aux->next;
	aux->next = new_node;
	return (new_node);
}
