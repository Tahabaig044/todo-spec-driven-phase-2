"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.todoSpecs = void 0;
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
exports.todoSpecs = todoSpecs;
//# sourceMappingURL=todo.spec.js.map