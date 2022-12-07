#include <Python.h>
#include <stdio.h>



/**
 * print_python_bytes - Display basic information about a bytes.
 * @p: bytes.
 *
 */

void print_python_bytes(PyObject *p)
{
	int i;
	char *str;

	printf("[.] bytes object info\n");
	if (!(PyBytes_Check(p)))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", PyBytes_Size(p));
	printf("  trying string: %s\n", PyBytes_AsString(p));
	str = PyBytes_AsString(p);
	if (PyBytes_Size(p) > 10)
		printf("  first 10 bytes: ");
	else
		printf("  first %ld bytes: ", PyBytes_Size(p) + 1);
	for (i = 0; i < (PyBytes_Size(p) + 1) && i < 10; i++)
	{
		if (i != PyBytes_Size(p) && i != 9)
		{
			if (str[i] == 0)
				printf("00 ");
			else
				printf("%hhx ", str[i]);
		}
		else
		{
			if (str[i] == 0)
				printf("00\n");
			else
				printf("%hhx\n", str[i]);
		}
	}
}

/**
 * print_python_list - Display basic information about a list.
 * @p: List.
 *
 */

void print_python_list(PyObject *p)
{
	int i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %d: %s\n", i, PyList_GET_ITEM(p, i)->ob_type->tp_name);
		if (strcmp(PyList_GET_ITEM(p, i)->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(PyList_GET_ITEM(p, i));
	}
}
