/**
 * Todo API Specification
 *
 * This specification defines the API endpoints for the Todo application
 * as part of the Panaversity Hackathon II project.
 */

// API Specification
interface TodoApiSpec {
  endpoints: {
    // GET /api/todos - Retrieve all todos
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
            createdAt: string; // ISO date string
            updatedAt: string; // ISO date string
            dueDate?: string;  // ISO date string
          }>;
        };
      };
      errors: [
        { status: 500; message: 'Internal server error' }
      ];
    };

    // POST /api/todos - Create a new todo
    create: {
      method: 'POST';
      path: '/api/todos';
      description: 'Creates a new todo item';
      requestBody: {
        title: string;
        description?: string;
        dueDate?: string; // ISO date string
      };
      response: {
        status: 201;
        body: {
          id: string;
          title: string;
          description?: string;
          completed: boolean;
          createdAt: string; // ISO date string
          updatedAt: string; // ISO date string
          dueDate?: string;  // ISO date string
        };
      };
      errors: [
        { status: 400; message: 'Invalid request body' },
        { status: 500; message: 'Internal server error' }
      ];
    };

    // GET /api/todos/:id - Retrieve a specific todo
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
          createdAt: string; // ISO date string
          updatedAt: string; // ISO date string
          dueDate?: string;  // ISO date string
        };
      };
      errors: [
        { status: 404; message: 'Todo not found' },
        { status: 500; message: 'Internal server error' }
      ];
    };

    // PUT /api/todos/:id - Update a specific todo
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
        dueDate?: string; // ISO date string
      };
      response: {
        status: 200;
        body: {
          id: string;
          title: string;
          description?: string;
          completed: boolean;
          createdAt: string; // ISO date string
          updatedAt: string; // ISO date string
          dueDate?: string;  // ISO date string
        };
      };
      errors: [
        { status: 404; message: 'Todo not found' },
        { status: 400; message: 'Invalid request body' },
        { status: 500; message: 'Internal server error' }
      ];
    };

    // PATCH /api/todos/:id/complete - Mark todo as completed
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
          createdAt: string; // ISO date string
          updatedAt: string; // ISO date string
          dueDate?: string;  // ISO date string
        };
      };
      errors: [
        { status: 404; message: 'Todo not found' },
        { status: 500; message: 'Internal server error' }
      ];
    };

    // DELETE /api/todos/:id - Delete a specific todo
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
        { status: 404; message: 'Todo not found' },
        { status: 500; message: 'Internal server error' }
      ];
    };
  };
}

// Validation rules for API
const apiValidationSpecs = {
  "Request Validation": {
    "title required for creation": true,
    "title minimum length": 1,
    "title maximum length": 255,
    "dueDate format": "ISO 8601 date string"
  },

  "Response Validation": {
    "all dates in ISO format": true,
    "required fields present": true,
    "consistent data types": true
  },

  "Error Handling": {
    "proper error status codes": true,
    "consistent error response format": true,
    "descriptive error messages": true
  }
};

export { TodoApiSpec, apiValidationSpecs };