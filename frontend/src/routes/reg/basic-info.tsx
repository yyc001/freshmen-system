import { createFileRoute, redirect } from '@tanstack/react-router'
import PageContent from '../../components/PageContent'
import axios from 'axios';
import DynamicForm from '../../components/DynamicForm';
import Title from 'antd/es/typography/Title';
import { Form, Input } from 'antd';

// const onFinishFailed: FormProps["onFinishFailed"] = (errorInfo) => {
//   console.log('Failed:', errorInfo);
//   alert(errorInfo.errorFields[0].errors[0]);
// };

export const Route = createFileRoute('/reg/basic-info')({
  loader: async (params : any) => {
    params = params.location.search;
    let uid = params.uid;
    if (!uid && !params.notice) {
      throw redirect({to: '/reg/notice'});
    }
    if (!uid) {
      const response = await axios.get('/api/whoami');
      uid = response.data.uid;
    }
    const response = await axios.get('/api/student/info/get', {params: {uid: uid}});
    return Object.assign({uid: uid}, response.data)
  },
  component: () => {
    const loader_data = Route.useLoaderData();

    return (
      <>
      <PageContent>
        
        <Title level={2}> 报名 · 第二步</Title>
        <DynamicForm 
          getFields={function (setFields: any): void {
            axios.get('/api/student/info/fields').then((response) => {
              setFields(response.data.fields);
            });
          } } 
          onFinish={function (values: any): void {
            console.log(values)
            axios.post('/api/student/info/set', values)
            .then(response => {
              alert(JSON.stringify(response.data))
              window.location.href = "/reg/service-hall"
            })
            .catch((error: any) => {
              alert(JSON.stringify(error.response.data))
            })
          } } 
          initialValues={loader_data} >
          <Form.Item name="uid"> <Input type="hidden" defaultValue={loader_data.uid}/> </Form.Item>
          </DynamicForm>
      </PageContent>
      </>
    )
  },
})
