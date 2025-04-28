import dagger
from dagger import dag, function, object_type


@object_type
class FfmpegAgent:
    @function
    def ffmpeg_tool(self, command: str, source_directory_arg: dagger.Directory) -> dagger.Container:
        """
        Can convert multimedia files with ffmpeg

        Args:
            command: The command to execute
            source_directory_arg: The directory containing the input files
        Returns:
            A container with the specified command and the output directory
        """

        return (dag.container()
                .from_("jrottenberg/ffmpeg")
                .with_mounted_directory("/app", source_directory_arg)
                .with_workdir("/app")
                .with_exec(command)
        )



    @function
    def ffmpeg_task(self, task: str, source_directory_arg: dagger.Directory) -> dagger.Directory:
        """Returns a Directory containing the output of the ffmpeg task"""

        container = (dag.container()
                     .from_("jrottenberg/ffmpeg")
                     .with_mounted_directory("/app", source_directory_arg)
                     .with_workdir("/app"))

        environment = (
            dag.env()
            .with_string_input("task", task, "the task to complete")
            .with_container_input(
                "builder",
                container,
                "a container to use for executing the ffmpeg task",
            )
            .with_container_output(
                "completed", "the output directory of the ffmpeg task is /app"
            )
        )

        work = (
            dag.llm()
            .with_env(environment)
            .with_prompt_file(dag.current_module().source().file("prompt.txt"))
        )

        return work.env().output("completed").as_container().directory('/app')


