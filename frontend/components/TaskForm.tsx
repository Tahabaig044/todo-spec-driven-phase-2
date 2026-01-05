'use client';

import { useState, FormEvent } from 'react';
import { TaskInput } from '../types/task';
import { useTaskContext } from '../context/TaskContext';

export default function TaskForm() {
  const { addTask } = useTaskContext();
  const [input, setInput] = useState<TaskInput>({ title: '', description: '' });
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    if (!input.title.trim()) return;

    setLoading(true);
    try {
      await addTask(input);
      setInput({ title: '', description: '' });
    } catch (error) {
      console.error('Error adding task:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="mb-8 p-6 bg-white rounded-lg shadow-md">
      <h2 className="text-xl font-semibold mb-4 text-gray-700">Add New Task</h2>
      <div className="mb-4">
        <label htmlFor="title" className="block text-gray-700 font-medium mb-2">
          Title *
        </label>
        <input
          type="text"
          id="title"
          value={input.title}
          onChange={(e) => setInput({ ...input, title: e.target.value })}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="Enter task title"
          required
        />
      </div>
      <div className="mb-4">
        <label htmlFor="description" className="block text-gray-700 font-medium mb-2">
          Description
        </label>
        <textarea
          id="description"
          value={input.description}
          onChange={(e) => setInput({ ...input, description: e.target.value })}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="Enter task description (optional)"
          rows={3}
        />
      </div>
      <button
        type="submit"
        disabled={loading}
        className={`px-4 py-2 rounded-md text-white font-medium ${
          loading ? 'bg-gray-400' : 'bg-blue-500 hover:bg-blue-600'
        } transition-colors`}
      >
        {loading ? 'Adding...' : 'Add Task'}
      </button>
    </form>
  );
}