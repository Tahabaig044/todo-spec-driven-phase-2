interface TodoApiSpec {
    endpoints: {
        getAll: {
            method: 'GET';
            path: '/api/todos';
            description: 'Retrieves all todo items';
            response: {
                status: 200;
                body: {
                    todos: Array<{
                        id: string;
                        title: string;
                        description?: string;
                        completed: boolean;
                        createdAt: string;
                        updatedAt: string;
                        dueDate?: string;
                    }>;
                };
            };
            errors: [
                {
                    status: 500;
                    message: 'Internal server error';
                }
            ];
        };
        create: {
            method: 'POST';
            path: '/api/todos';
            description: 'Creates a new todo item';
            requestBody: {
                title: string;
                description?: string;
                dueDate?: string;
            };
            response: {
                status: 201;
                body: {
                    id: string;
                    title: string;
                    description?: string;
                    completed: boolean;
                    createdAt: string;
                    updatedAt: string;
                    dueDate?: string;
                };
            };
            errors: [
                {
                    status: 400;
                    message: 'Invalid request body';
                },
                {
                    status: 500;
                    message: 'Internal server error';
                }
            ];
        };
        getById: {
            method: 'GET';
            path: '/api/todos/:id';
            description: 'Retrieves a specific todo by ID';
            params: {
                id: string;
            };
            response: {
                status: 200;
                body: {
                    id: string;
                    title: string;
                    description?: string;
                    completed: boolean;
                    createdAt: string;
                    updatedAt: string;
                    dueDate?: string;
                };
            };
            errors: [
                {
                    status: 404;
                    message: 'Todo not found';
                },
                {
                    status: 500;
                    message: 'Internal server error';
                }
            ];
        };
        update: {
            method: 'PUT';
            path: '/api/todos/:id';
            description: 'Updates a specific todo by ID';
            params: {
                id: string;
            };
            requestBody: {
                title?: string;
                description?: string;
                completed?: boolean;
                dueDate?: string;
            };
            response: {
                status: 200;
                body: {
                    id: string;
                    title: string;
                    description?: string;
                    completed: boolean;
                    createdAt: string;
                    updatedAt: string;
                    dueDate?: string;
                };
            };
            errors: [
                {
                    status: 404;
                    message: 'Todo not found';
                },
                {
                    status: 400;
                    message: 'Invalid request body';
                },
                {
                    status: 500;
                    message: 'Internal server error';
                }
            ];
        };
        complete: {
            method: 'PATCH';
            path: '/api/todos/:id/complete';
            description: 'Marks a specific todo as completed';
            params: {
                id: string;
            };
            response: {
                status: 200;
                body: {
                    id: string;
                    title: string;
                    description?: string;
                    completed: boolean;
                    createdAt: string;
                    updatedAt: string;
                    dueDate?: string;
                };
            };
            errors: [
                {
                    status: 404;
                    message: 'Todo not found';
                },
                {
                    status: 500;
                    message: 'Internal server error';
                }
            ];
        };
        delete: {
            method: 'DELETE';
            path: '/api/todos/:id';
            description: 'Deletes a specific todo by ID';
            params: {
                id: string;
            };
            response: {
                status: 204;
                body: null;
            };
            errors: [
                {
                    status: 404;
                    message: 'Todo not found';
                },
                {
                    status: 500;
                    message: 'Internal server error';
                }
            ];
        };
    };
}
declare const apiValidationSpecs: {
    "Request Validation": {
        "title required for creation": boolean;
        "title minimum length": number;
        "title maximum length": number;
        "dueDate format": string;
    };
    "Response Validation": {
        "all dates in ISO format": boolean;
        "required fields present": boolean;
        "consistent data types": boolean;
    };
    "Error Handling": {
        "proper error status codes": boolean;
        "consistent error response format": boolean;
        "descriptive error messages": boolean;
    };
};
export { TodoApiSpec, apiValidationSpecs };
//# sourceMappingURL=todo-api.spec.d.ts.map