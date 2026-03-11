import { Dropzone } from "@mantine/dropzone";
import { Text } from "@mantine/core";

export const UploadFile = () => {
  return (
    <Dropzone
      multiple={false}
      onDrop={(files) => {
        console.log("files", files);
      }}
    >
      <div>
        <Text>Загрузите подпись</Text>
      </div>
    </Dropzone>
  );
};
