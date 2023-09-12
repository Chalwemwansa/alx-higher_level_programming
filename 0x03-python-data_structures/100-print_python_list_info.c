#include <stdio.h>
#include <stdlib.h>
#include "object.h"
#include "listobject.h"

/**
 * print_python_list_info - prints the info on a python list
 *
 * @p: THE agument passsed to the function
 * Return: void, does not return anything
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *newlist = (PyListObject *)p;
	PyVarObject *varlist = (PyVarObject *)p;
	PyObject **items = newlist->ob_item;
	int i;

	printf("[*] Size of the Python List = %zd\n", Py_SIZE(varlist));
	printf("[*] Allocated = %zd\n", newlist->allocated);
	for (i = 0; i < Py_SIZE(varlist); i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(items[i])->tp_name);
	}
}
