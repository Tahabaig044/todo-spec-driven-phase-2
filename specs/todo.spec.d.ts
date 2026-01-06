interface Todo {
    id: string;
    title: string;
    description?: string;
    completed: boolean;
    createdAt: Date;
    updatedAt: Date;
    dueDate?: Date;
}
interface TodoService {
    createTodo(title: string, description?: string): Promise<Todo>;
    getAllTodos(): Promise<Todo[]>;
    getTodoById(id: string): Promise<Todo | null>;
    updateTodo(id: string, updates: Partial<Todo>): Promise<Todo | null>;
    completeTodo(id: string): Promise<Todo | null>;
    deleteTodo(id: string): Promise<boolean>;
}
declare const todoSpecs: {
    "Todo Creation": {
        "should require a title": boolean;
        "should generate a unique ID": boolean;
        "should set default completion status to false": boolean;
        "should set creation timestamp": boolean;
        "should allow optional description": boolean;
    };
    "Todo Retrieval": {
        "should return all todos": boolean;
        "should return specific todo by ID": boolean;
        "should return null for non-existent todo": boolean;
    };
    "Todo Update": {
        "should update specified fields only": boolean;
        "should update modification timestamp": boolean;
        "should not modify other fields": boolean;
    };
    "Todo Completion": {
        "should mark todo as completed": boolean;
        "should update modification timestamp": boolean;
    };
    "Todo Deletion": {
        "should remove todo from storage": boolean;
        "should return success indicator": boolean;
    };
};
export { Todo, TodoService, todoSpecs };
//# sourceMappingURL=todo.spec.d.ts.map