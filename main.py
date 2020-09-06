#!/usr/bin/env python3

from gql import gql
import wandb
from typing import Dict

def get_sweep_table(api: wandb.Api, project: str) -> Dict[str, str]:
    QUERY = gql('''       
    query Sweep($project: String!, $entity: String) {
        project(name: $project, entityName: $entity) {
            sweeps {
                edges {
                    node {
                        name
                        displayName
                        config
                    }
                }
            }
        }
    }''')

    entity, project = project.split("/")
    response = api.client.execute(QUERY, variable_values={
        'entity': entity,
        'project': project,
    })

    edges = response.get("project", {}).get("sweeps", {}).get("edges")
    assert edges

    id_to_name  = {}
    for sweep in edges:
        sweep = sweep["node"]

        name = sweep["displayName"]
        if name is None:
            name = [s for s in sweep["config"].split("\n") if s.startswith("name:")]
            assert len(name)==1
            name = name[0].split(":")[1].strip()

        id_to_name[sweep["name"]] = name

    return id_to_name


api = wandb.Api()
print(get_sweep_table(api, "username/project_name"))
