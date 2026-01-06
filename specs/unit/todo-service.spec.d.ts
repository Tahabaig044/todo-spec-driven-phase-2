import { Todo, TodoService } from '../todo.spec';
declare class MockTodoService implements TodoService {
    private todos;
    createTodo(title: string, description?: string): Promise<Todo>;
    getAllTodos(): Promise<Todo[]>;
    getTodoById(id: string): Promise<Todo | null>;
    updateTodo(id: string, updates: Partial<Todo>): Promise<Todo | null>;
    completeTodo(id: string): Promise<Todo | null>;
    deleteTodo(id: string): Promise<boolean>;
}
declare const todoServiceUnitTests: {
    createTodo: string[];
    getAllTodos: string[];
    getTodoById: string[];
    updateTodo: string[];
    completeTodo: string[];
    deleteTodo: string[];
};
export { MockTodoService, todoServiceUnitTests };
//# sourceMappingURL=todo-service.spec.d.ts.map