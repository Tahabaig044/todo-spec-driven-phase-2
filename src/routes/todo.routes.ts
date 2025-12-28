/**
 * Todo Routes Implementation
 *
 * This file defines the API routes as specified
 * in the todo-api.spec.ts file.
 *
 * Implementation follows the spec-driven development approach
 * where this implementation is driven by the specification.
 */

import { Router } from 'express';
import { TodoController } from '../controllers/todo.controller';

const router = Router();
const todoController = new TodoController();

// GET /api/todos - Retrieve all todos
router.get('/', (req, res) => {
  // Implementation will be completed based on specification
  todoController.getAllTodos(req, res);
});

// POST /api/todos - Create a new todo
router.post('/', (req, res) => {
  // Implementation will be completed based on specification
  todoController.createTodo(req, res);
});

// GET /api/todos/:id - Retrieve a specific todo
router.get('/:id', (req, res) => {
  // Implementation will be completed based on specification
  todoController.getTodoById(req, res);
});

// PUT /api/todos/:id - Update a specific todo
router.put('/:id', (req, res) => {
  // Implementation will be completed based on specification
  todoController.updateTodo(req, res);
});

// PATCH /api/todos/:id/complete - Mark todo as completed
router.patch('/:id/complete', (req, res) => {
  // Implementation will be completed based on specification
  todoController.completeTodo(req, res);
});

// DELETE /api/todos/:id - Delete a specific todo
router.delete('/:id', (req, res) => {
  // Implementation will be completed based on specification
  todoController.deleteTodo(req, res);
});

export default router;