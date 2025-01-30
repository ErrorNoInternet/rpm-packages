print(
    " AND ".join(
        f"({license})" if " " in license else license
        for license in sorted(
            set(
                filter(
                    None,
                    map(
                        lambda line: line.split(": ")[0].lstrip("# "),
                        open(0).read().splitlines(),
                    ),
                )
            )
        )
    )
)
