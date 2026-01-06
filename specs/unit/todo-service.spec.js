"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.todoServiceUnitTests = exports.MockTodoService = void 0;
class MockTodoService {
    constructor() {
        this.todos = [];
    }
    async createTodo(title, description) {
        throw new Error('Method not implemented');
    }
    async getAllTodos() {
        throw new Error('Method not implemented');
    }
    async getTodoById(id) {
        throw new Error('Method not implemented');
    }
    async updateTodo(id, updates) {
        throw new Error('Method not implemented');
    }
    async completeTodo(id) {
        throw new Error('Method not implemented');
    }
    async deleteTodo(id) {
        throw new Error('Method not implemented');
    }
}
exports.MockTodoService = MockTodoService;
const todoServiceUnitTests = {
    "createTodo": [
        "should create a new todo with provided title",
        "should generate a unique ID for the new todo",
        "should set completion status to false by default",
        "should set creation and update timestamps",
        "should allow optional description",
        "should throw error if title is empty"
    ],
    "getAllTodos": [
        "should return all existing todos",
        "should return empty array if no todos exist",
        "should return todos in creation order"
    ],
    "getTodoById": [
        "should return todo with matching ID",
        "should return null if no todo matches ID",
        "should not modify the returned todo"
    ],
    "updateTodo": [
        "should update only specified fields",
        "should update the modification timestamp",
        "should return updated todo",
        "should return null if todo doesn't exist"
    ],
    "completeTodo": [
        "should mark todo as completed",
        "should update the modification timestamp",
        "should return updated todo",
        "should return null if todo doesn't exist"
    ],
    "deleteTodo": [
        "should remove todo from storage",
        "should return true for successful deletion",
        "should return false if todo doesn't exist"
    ]
};
exports.todoServiceUnitTests = todoServiceUnitTests;
//# sourceMappingURL=todo-service.spec.js.map