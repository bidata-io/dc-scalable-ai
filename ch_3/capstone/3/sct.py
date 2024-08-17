traced_output = loaded_traced_model(sample_input)
assert torch.allclose(traced_output, loaded_output), "Traced model output should match the loaded model output."

Ex().success_msg("All checks passed successfully.")
