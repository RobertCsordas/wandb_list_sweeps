# List Weights and Biases sweeps by their name

W&B handles sweeps by their ID. However the ID is generated randomly, so if one wants to automatize the analysis process, it needs to query the seeds based on their string name. The official API does not support this however.

This code is based on reverse engineering the API used by the website when rendering the sweep table.

# Usage

```python
def get_sweep_table(api: wandb.Api, project: str) -> Dict[str, str]
```

Arguments:
- ```api``` the standard API object used to query wandb runs
- ```project``` 'entity/project_name'. Entity is usually your username

Return: A dict of sweep ID, name pairs.

# Using the result for getting a sweep list

```python
api.runs(project, {"sweep": sweep_id})
```

In case of multiple sweep ids in an array:

```python
api.runs(project, {"sweep": {"$in": sweep_id_list}})
```
