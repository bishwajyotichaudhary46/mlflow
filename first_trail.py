import mlflow

def calculate_sum(x,y):
    return x*y

if __name__=="__main__":
    # starting server of the mlflow
    with mlflow.start_run():
        x,y = 75,10
        z=calculate_sum(x,y)
        # tracking the experiments with mlfow
        mlflow.log_param("x",x)
        mlflow.log_param("y",y)
        mlflow.log_metric("z",z)

