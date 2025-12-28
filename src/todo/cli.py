import argparse
import sys
from src.todo.service import todo_service, TodoNotFoundException

def main():
    parser = argparse.ArgumentParser(description="Todo CLI Application")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new todo item")
    add_parser.add_argument("title", type=str, help="Title of the todo item")
    add_parser.add_argument("--description", type=str, help="Optional description of the todo item", default=None)

    # Update command (placeholder for now)
    update_parser = subparsers.add_parser("update", help="Update an existing todo item")
    update_parser.add_argument("id", type=int, help="ID of the todo item to update")
    update_parser.add_argument("--title", type=str, help="New title for the todo item", default=None)
    update_parser.add_argument("--description", type=str, help="New description for the todo item", default=None)

    # Mark status command
    mark_status_parser = subparsers.add_parser("mark-status", help="Mark a todo item as complete or incomplete")
    mark_status_parser.add_argument("id", type=str, help="ID of the todo item to update")
    mark_status_parser.add_argument("--status", type=str, required=True, choices=['complete', 'incomplete'], help="New status for the todo item (complete or incomplete)")

    # List command
    list_parser = subparsers.add_parser("list", help="List all todo items")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a todo item")
    delete_parser.add_argument("id", type=int, help="ID of the todo item to delete")

    args = parser.parse_args()

    if args.command == "add":
        try:
            todo = todo_service.add_todo(args.title, args.description)
            print(f"Todo added:")
            print(f"  ID: {todo.id}")
            print(f"  Title: \"{todo.title}\"")
            if todo.description:
                print(f"  Description: \"{todo.description}\"")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.command == "update":
        if args.title is None and args.description is None:
            print("Error: Nothing to update. Please provide --title or --description.", file=sys.stderr)
            sys.exit(1)
        
        try:
            updated_todo = todo_service.update_todo(args.id, args.title, args.description)
            
            if updated_todo:
                print(f"Todo {updated_todo.id} updated successfully:")
                print(f"  ID: {updated_todo.id}")
                print(f"  Title: \"{updated_todo.title}\"")
                if updated_todo.description is not None:
                    print(f"  Description: \"{updated_todo.description}\"")
                else:
                    print(f"  Description: \"\"") # Display empty if description is None
            else:
                print(f"Error: Todo with ID {args.id} not found.", file=sys.stderr)
                sys.exit(1)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.command == "mark-status":
        try:
            todo_id = int(args.id) # Manual conversion
            completed_status = True if args.status == "complete" else False
            updated_todo = todo_service.update_todo_status(todo_id, completed_status)
            print(f"Todo {updated_todo.id} marked as {args.status}.")
        except ValueError as e:
            # Check if the ValueError is due to invalid integer conversion
            # The error message from int() conversion is typically "invalid literal for int() with base 10: 'abc'"
            if "invalid literal for int()" in str(e):
                print(f"Error: {args.id} is not a valid integer for Todo ID.", file=sys.stderr)
            else: # Other ValueErrors from service.py (e.g., "Todo with ID X not found.")
                print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.command == "list":
        todos = todo_service.get_all_todos()
        if not todos:
            print("No todo items found.")
        else:
            print("Todo List:")
            for todo in todos:
                status = "✓" if todo.completed else " "
                description_line = f"    Description: \"{todo.description}\"" if todo.description else ""
                print(f"  [{status}] ID: {todo.id}, Title: \"{todo.title}\"")
                if description_line:
                    print(description_line)
    elif args.command == "delete":
        try:
            todo_service.delete_todo(args.id)
            print(f"Todo with ID {args.id} deleted successfully.")
        except TodoNotFoundException:
            print(f"Error: Todo with ID {args.id} not found.", file=sys.stderr)
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
