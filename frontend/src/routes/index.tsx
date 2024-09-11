import { createFileRoute, redirect } from '@tanstack/react-router'
import PageContent from '../components/PageContent'
import { Button } from 'antd'
import axios from 'axios';

export const Route = createFileRoute('/')({
  loader: async () => {
    try{
      const user_res = await axios.get('/api/whoami');
      const global_res = await axios.get('/api/global/get');
      return {
        user: user_res.data,
        global: global_res.data
      }
    }
    catch (e) {
      throw redirect({to: '/help'})
    }
  },
  
  component: () => {
    const loader_data = Route.useLoaderData();

    return (
      <>
      <PageContent>
        <h1> 泰山学堂新生报名系统 </h1>
        <hr />
        <p>{loader_data.user.uid} - {loader_data.user.name}</p>
        <p> 报名开始时间： {loader_data.global.start_time}</p>
        <p> 报名截止时间： {loader_data.global.end_time}</p>
        <p><Button href='/reg/ready-submit'>我的报名状态</Button></p>
        <Button type='primary' href='/reg/contact-details'> 开始报名 </Button>
      </PageContent>
      </>
    )
  },
})
