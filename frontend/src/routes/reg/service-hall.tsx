import { createFileRoute } from '@tanstack/react-router'
import PageContent from '../../components/PageContent'
import { Button, Form, Input, Space } from 'antd'
import axios from 'axios'

const onFinish = (value: any) => {
  console.log(value)
  axios.post('/api/student/info/set', value)
  .then(response => {
    alert(JSON.stringify(response.data))
    window.location.href = "/reg/attachments"
  })
  .catch((error: any) => {
    alert(JSON.stringify(error.response.data))
  })
}

export const Route = createFileRoute('/reg/service-hall')({
  loader: async (params : any) => {
    params = params.location.search;
    console.log(params)
    let uid = params.uid;
    if (!uid) {
      const response = await axios.get('/api/whoami');
      uid = response.data.uid;
    }
    const response = await axios.get('/api/student/info/get', {params: {uid: uid}});
    return Object.assign({uid: uid}, response.data)
  },
  component: () => {
    const loader_data = Route.useLoaderData();
    console.log(loader_data)
    return (
      <>
    <PageContent>
        <h1> 报名 · 第三步 </h1>
        <Form
          name="basic"
          labelCol={{ span: 8 }}
          wrapperCol={{ span: 16 }}
          style={{ maxWidth: 600 }}
          layout="horizontal"
          variant="filled"
          initialValues={loader_data}
          autoComplete="off"
          onFinish={onFinish}
        >
          <h2> 服务大厅登记 </h2>
          <Form.Item hidden name="uid"/>
          <Form.Item
            label="申请编号"
            name="service_hall_app_no"
          >
            <Input maxLength={20}/>
          </Form.Item>
          <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
            <Space>
                <Button href='/reg/basic-info'>上一步</Button>
                <Button type="primary" htmlType="submit">下一步</Button>
            </Space>
          </Form.Item>
        </Form>
      </PageContent>
      </>
    )
  },
})