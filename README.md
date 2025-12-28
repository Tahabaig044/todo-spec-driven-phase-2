# Todo Spec-Driven Application

A spec-driven todo application built for Panaversity Hackathon II. This project follows a specification-driven development approach where specifications drive the implementation.

## Project Structure

```
todo-spec-driven/
├── src/                    # Source code implementation
│   ├── components/         # UI components (if applicable)
│   ├── controllers/        # API controllers
│   ├── models/             # Data models
│   ├── routes/             # API routes
│   ├── services/           # Business logic services
│   └── utils/              # Utility functions
├── specs/                  # Specifications and requirements
│   ├── unit/               # Unit test specifications
│   ├── integration/        # Integration test specifications
│   └── e2e/                # End-to-end test specifications
├── tests/                  # Actual test implementations
│   ├── unit/               # Unit tests
│   ├── integration/        # Integration tests
│   └── e2e/                # End-to-end tests
├── config/                 # Configuration files
├── docs/                   # Documentation
└── utils/                  # Project utilities
```

## Spec-Driven Development Approach

This project implements a spec-driven development approach:

1. **Specifications First**: Requirements and API contracts are defined first in the `specs/` directory
2. **Implementation Driven**: Code is written to satisfy the specifications
3. **Test Verification**: Tests verify that implementation matches specifications

## Getting Started

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   npm install
   ```

### Running the Application

```bash
# Development mode
npm run dev

# Build for production
npm run build

# Run tests
npm test
```

## API Endpoints

The application provides the following API endpoints:

- `GET /api/todos` - Retrieve all todos
- `POST /api/todos` - Create a new todo
- `GET /api/todos/:id` - Retrieve a specific todo
- `PUT /api/todos/:id` - Update a specific todo
- `PATCH /api/todos/:id/complete` - Mark a todo as completed
- `DELETE /api/todos/:id` - Delete a specific todo
- `GET /health` - Health check endpoint

## Panaversity Hackathon II Guidelines

This project follows the Panaversity Hackathon II guidelines:

- Spec-driven development approach
- Clean architecture
- Comprehensive testing
- Proper documentation
- Well-structured code

## Configuration

Environment variables can be configured in the `.env` file:

- `NODE_ENV` - Node environment (development, production)
- `PORT` - Server port (default: 3000)
- `DATABASE_URL` - Database connection string

## Scripts

- `npm start` - Start the production server
- `npm run dev` - Start the development server with hot reloading
- `npm run build` - Compile TypeScript to JavaScript
- `npm test` - Run tests
- `npm run test:watch` - Run tests in watch mode
- `npm run test:coverage` - Run tests with coverage report
- `npm run lint` - Lint the code
- `npm run lint:fix` - Fix linting issues automatically

## Contributing

1. Define specifications in the `specs/` directory
2. Implement code to satisfy the specifications
3. Write tests to verify the implementation
4. Submit a pull request

## License

This project is licensed under the MIT License.