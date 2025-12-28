/**
 * Entry Point for Todo Application
 *
 * This is the main entry point for the spec-driven todo application.
 */

import app from './app';

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Todo application server is running on port ${PORT}`);
  console.log(`Health check available at http://localhost:${PORT}/health`);
  console.log('Spec-driven development approach initialized successfully');
});