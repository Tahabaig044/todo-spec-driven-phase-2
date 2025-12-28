/**
 * Todo Application Specification
 *
 * This specification defines the requirements for the Todo application
 * as part of the Panaversity Hackathon II project.
 *
 * The application should implement a spec-driven development approach
 * where specifications drive the implementation.
 */

// Core Todo Entity Specification
interface Todo {
  id: string;
  title: string;
  description?: string;
  completed: boolean;
  createdAt: Date;
  updatedAt: Date;
  dueDate?: Date;
}

// Todo Service Specification
interface TodoService {
  /**
   * Creates a new todo item
   * @param title - The title of the todo
   * @param description - Optional description
   * @returns Promise containing the created Todo
   */
  createTodo(title: string, description?: string): Promise<Todo>;

  /**
   * Retrieves all todo items
   * @returns Promise containing array of todos
   */
  getAllTodos(): Promise<Todo[]>;

  /**
   * Retrieves a specific todo by ID
   * @param id - The ID of the todo to retrieve
   * @returns Promise containing the Todo or null
   */
  getTodoById(id: string): Promise<Todo | null>;

  /**
   * Updates an existing todo
   * @param id - The ID of the todo to update
   * @param updates - The fields to update
   * @returns Promise containing the updated Todo or null
   */
  updateTodo(id: string, updates: Partial<Todo>): Promise<Todo | null>;

  /**
   * Marks a todo as completed
   * @param id - The ID of the todo to mark as completed
   * @returns Promise containing the updated Todo or null
   */
  completeTodo(id: string): Promise<Todo | null>;

  /**
   * Deletes a todo by ID
   * @param id - The ID of the todo to delete
   * @returns Promise indicating success
   */
  deleteTodo(id: string): Promise<boolean>;
}

// Expected behavior specifications
const todoSpecs = {
  "Todo Creation": {
    "should require a title": true,
    "should generate a unique ID": true,
    "should set default completion status to false": true,
    "should set creation timestamp": true,
    "should allow optional description": true
  },

  "Todo Retrieval": {
    "should return all todos": true,
    "should return specific todo by ID": true,
    "should return null for non-existent todo": true
  },

  "Todo Update": {
    "should update specified fields only": true,
    "should update modification timestamp": true,
    "should not modify other fields": true
  },

  "Todo Completion": {
    "should mark todo as completed": true,
    "should update modification timestamp": true
  },

  "Todo Deletion": {
    "should remove todo from storage": true,
    "should return success indicator": true
  }
};

export { Todo, TodoService, todoSpecs };