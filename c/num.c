#include <Python.h>

static PyObject* pgcd(PyObject* self,PyObject* args) {
    unsigned long long a,b;
    if (!PyArg_ParseTuple(args,"KK",&a,&b)) return NULL;
    while (a > 1 && b > 1) {
        if (a > b) a = a % b;
        else b = b % a;
    }
    unsigned long long resultat = 0;
    if (a == 1 || b == 1) resultat = 1;
    if (a == 0) resultat = b;
    if (b == 0) resultat = a;
	return Py_BuildValue("K",resultat);
}

static PyMethodDef numbers_methods[] = {
    {"pgcd",pgcd, METH_VARARGS,
     "calcule le pgcd de deux nombres"},
    {NULL, NULL, 0, NULL}        
};

static struct PyModuleDef numbers_module = {
    PyModuleDef_HEAD_INIT,
    "num",   
    NULL, 
    -1,       
	numbers_methods
};

PyMODINIT_FUNC PyInit_num(void) {
    return PyModule_Create(&numbers_module);
}
