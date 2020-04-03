def get_actions_defined(workflow_json):
    action_names = []
    for key, vals in workflow_json.items():
      if type(vals) is dict:
        all_tasks = vals.get('tasks')
        for task, details in all_tasks.items():
          if details.get('action') is not None:
            action_names.append({'name': details.get('action'), 'input': list(details.get('input').keys()) if details.get('input') else []})
    return action_names

my_dict = {
  "version": "2.0",
  "my_python_workflow122": {
    "type": "direct",
    "tasks": {
      "my_action_task": {
        "action": "sporact.demo_action10",
        "input": {
          "ip_address": "104.27.163.228",
          "dudu": "12345678"
        }
      }
    }
  }
}

print(get_actions_defined(my_dict))
