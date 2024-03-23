import { createFileRoute } from '@tanstack/react-router'
import PageContent from '../../components/PageContent'
import { Button, Form, Input, Radio } from 'antd'
import axios from 'axios'

const onFinish = (value: any) => {
  axios.post('/api/student/check/set', value)
  .then((res) => {
    console.log(res)
  })

}

export const Route = createFileRoute('/manage/view/$uid')({
  loader: async (params : any) => {
    const uid = params.params.uid;
    const manual_check = await axios.get('/api/student/check/get', {params: {uid: uid}});
    console.log(manual_check.data)
    return Object.assign({uid: uid}, manual_check.data)
  },
  component: () => {
    const { uid }: any = Route.useParams()
    const loader_data = Route.useLoaderData();
    console.log(loader_data)
    return (
      <>
        <PageContent>
          <h1> 报名详情 </h1>
          <Button href={'/reg/basic-info?uid=' + uid} target='_blank'>查看报名信息</Button>
          <h1> 审核 </h1>
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
          <Form.Item hidden name="uid"/>
            
            <Form.Item
              label='审核结论'
              name='status'
            >
              <Radio.Group
                optionType="button"
                buttonStyle="solid"
                options={[
                  {
                    value: 2,
                    label: "通过"
                  },
                  {
                    value: 3,
                    label: "不通过"
                  }
                ]}
              />
            </Form.Item>
            <Form.Item
              label='审核意见'
              name='comment'
            >
              <Input/>
            </Form.Item>
            <Form.Item
              label='隐藏备注'
              name='private_comment'
            >
              <Input/>
            </Form.Item>
            <Button type="primary" htmlType="submit">提交</Button>
          </Form>
        </PageContent> 
      </>
    )
  },
})