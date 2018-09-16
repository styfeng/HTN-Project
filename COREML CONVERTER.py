import coremltools

coreml_model = coremltools.converters.keras.convert('my_model.h5')
print("successfully loaded keras model")

coreml_model.save('HeightWeight_model.mlmodel')
#coremltools.utils.save_spec(coreml_model, 'my_model.mlmodel')
print("successfully saved coreML model")