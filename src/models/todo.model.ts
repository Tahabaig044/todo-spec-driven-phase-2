/**
 * Todo Model Implementation
 *
 * This model implements the Todo interface as specified
 * in the todo.spec.ts file.
 *
 * Implementation follows the spec-driven development approach
 * where this implementation is driven by the specification.
 */

import { Todo } from '../../specs/todo.spec';
import { v4 as uuidv4 } from 'uuid';

class TodoModel implements Todo {
  id: string;
  title: string;
  description?: string;
  completed: boolean;
  createdAt: Date;
  updatedAt: Date;
  dueDate?: Date;

  constructor(title: string, description?: string, dueDate?: Date) {
    if (!title || title.trim().length === 0) {
      throw new Error('Title is required');
    }

    this.id = uuidv4();
    this.title = title;
    this.description = description;
    this.completed = false;
    this.createdAt = new Date();
    this.updatedAt = new Date();
    this.dueDate = dueDate;
  }

  // Method to update the todo
  update(updates: Partial<Todo>): void {
    // Update only the fields that are provided
    if (updates.title !== undefined) this.title = updates.title;
    if (updates.description !== undefined) this.description = updates.description;
    if (updates.completed !== undefined) this.completed = updates.completed;
    if (updates.dueDate !== undefined) this.dueDate = updates.dueDate;

    // Always update the modification timestamp
    this.updatedAt = new Date();
  }
}

export { TodoModel };