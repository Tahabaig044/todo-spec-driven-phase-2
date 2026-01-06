"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.apiValidationSpecs = void 0;
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
exports.apiValidationSpecs = apiValidationSpecs;
//# sourceMappingURL=todo-api.spec.js.map