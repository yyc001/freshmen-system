import { createFileRoute} from '@tanstack/react-router'
import PageContent from '../../components/PageContent'
import { Button, Form, Space, Upload } from 'antd'
import { UploadOutlined } from '@ant-design/icons';
import axios from 'axios';

// const onFinish = (value: any) => {
  // console.log("onfinish", value)
  // axios.post('/api/student/info/set', value)
  // .then(response => {
  //   alert(JSON.stringify(response.data))
  //   window.location.href = "/reg/service-hall"
  // })
  // .catch((error: any) => {
  //   alert(JSON.stringify(error.response.data))
  // })
// }

export const Route = createFileRoute('/reg/attachments')({
  loader: async (params : any) => {
    params = params.location.search;
    console.log(params)
    let uid = params.uid;
    if (!uid) {
      const response = await axios.get('/api/whoami');
      uid = response.data.uid;
    }
    const response = await axios.get('/api/student/attachments/get', {params: {uid: uid}});
    return Object.assign({uid: uid}, response.data)
  },
  component: () => {
    const loader_data = Route.useLoaderData();
    console.log(loader_data)
    return (
      <>
    <PageContent>
        <h1> 报名 · 第四步 </h1>
        <Form
          name="basic"
          labelCol={{ span: 8 }}
          wrapperCol={{ span: 16 }}
          style={{ maxWidth: 600 }}
          layout="horizontal"
          variant="filled"
          autoComplete="off"
          // onFinish={onFinish}
        >
          <h2> 附件 </h2>
          <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
            <Upload 
              action='/api/student/attachments/upload'
              onChange = {({ file }) => {
                if(file.status == "done") {
                  file.url = file.response.url
                  file.uid = file.response.uid
                  // console.log("done", file, fileList);
                }
              }}
              onRemove={(file) => {
                  axios.post('/api/student/attachments/remove', {id: file.uid})
                  // .then((res) => {console.log(res)})
                  // console.log("remove", file);
              }}
              // onDownload={(file) => {
              //   console.log(file)
              // }}
              // fileList={[]}
              defaultFileList={loader_data.attachments}
            >
              <Button icon={<UploadOutlined />}>Upload</Button>
            </Upload>
          </Form.Item>
          <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
            <Space>
                <Button href='/reg/service-hall'>上一步</Button>
                <Button href='/reg/ready-submit' type='primary'>下一步</Button>
            </Space>
          </Form.Item>
        </Form>
      </PageContent>
      </>
    )
  },
})