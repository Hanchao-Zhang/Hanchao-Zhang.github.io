# type: ignore
# flake8: noqa


# Plotting
fig = go.Figure()

# Generate and plot ellipses
for i in range(n):
    # Generate ellipse
    x, y, z = generate_ellipse(
        center=(0, 0, 0), radii=radii[i], rotation_angles=rotations[i]
    )

    # Add ellipse to plot
    fig.add_trace(
        go.Scatter3d(
            x=x, y=y, z=z, mode="lines", line=dict(color="blue"), name=f"Ellipse {i+1}"
        )
    )

    # add another ellipse
    x, y, z = generate_ellipse(
        center=(0, 0, 0), radii=radii2[i], rotation_angles=rotations2[i]
    )

    # Add ellipse to plot
    fig.add_trace(
        go.Scatter3d(
            x=x, y=y, z=z, mode="lines", line=dict(color="red"), name=f"Ellipse {i+1}"
        )
    )

    # add another ellipse
    x, y, z = generate_ellipse(
        center=(0, 0, 0), radii=radii3[i], rotation_angles=rotations3[i]
    )

    # Add ellipse to plot
    fig.add_trace(
        go.Scatter3d(
            x=x, y=y, z=z, mode="lines", line=dict(color="green"), name=f"Ellipse {i+1}"
        )
    )


# Update layout
fig.update_layout(
    scene=dict(xaxis_title="X Axis", yaxis_title="Y Axis", zaxis_title="Z Axis"),
    margin=dict(l=0, r=0, b=0, t=30),
)

fig.update_layout(showlegend=False)
# remove color_continuous_scale legend
fig.update_layout(coloraxis_showscale=False)
# fig.update_layout(width=800, height=650)

add_hyperplane(fig, [mean_rotation] * 3, "blue", "Hyperplane 1")
add_hyperplane(fig, [mean_rotation2] * 3, "red", "Hyperplane 2")
add_hyperplane(fig, [mean_rotation3] * 3, "green", "Hyperplane 3")

fig.show()



