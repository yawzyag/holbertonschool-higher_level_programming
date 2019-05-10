#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - info about list of python
 * @p: node
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	int list_size, i;
	PyObject *tp_element;

	list_size = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < list_size; i++)
	{
		tp_element = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(tp_element)->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	(void) p;
}
